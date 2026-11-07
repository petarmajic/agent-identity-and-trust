"""Draw the Agent Trust Gateway architecture and identity lifecycle scenario.

Run from the repository root: python scripts/draw_figures.py
Requires Matplotlib. The concept paper is in docs/product-concept.pdf.
"""

from pathlib import Path
from xml.etree import ElementTree as ET

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from matplotlib.path import Path as PlotPath

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
INK = "#222b34"
MUTED = "#526170"
RULE = "#cbd3db"
BLUE = "#356a94"
TEAL = "#2a7566"
PALE_BLUE = "#edf3f8"
PALE_GREEN = "#edf5f1"
PALE_GREY = "#f7f9fb"
RED = "#9b3f44"
PALE_RED = "#fbefef"

plt.rcParams.update({
    "font.family": "STIXGeneral",
    "font.size": 14,
    "text.color": INK,
    "svg.fonttype": "path",
    "svg.hashsalt": "agent-identity-product-architecture",
    "savefig.facecolor": "white",
})


def text(ax, x, y, value, size=14, **kwargs):
    return ax.text(x, y, value, fontsize=size,
                   ha=kwargs.pop("ha", "center"),
                   va=kwargs.pop("va", "center"), **kwargs)


def box(ax, x, y, width, height, title, body, fill=PALE_GREY,
        title_size=15, body_size=13, edge=RULE):
    ax.add_patch(Rectangle((x, y), width, height, facecolor=fill,
                           edgecolor=edge, linewidth=.8))
    text(ax, x + width / 2, y + 25, title, title_size, weight="bold")
    text(ax, x + width / 2, y + height / 2 + 15, body, body_size,
         color=MUTED, linespacing=1.3)


def arrow(ax, points, color=INK, dashed=False):
    ax.add_patch(FancyArrowPatch(path=PlotPath(points), arrowstyle="-|>",
                                mutation_scale=11, linewidth=1,
                                color=color, linestyle="--" if dashed else "-"))


def draw_platform():
    fig, ax = plt.subplots(figsize=(12, 6.85))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 1200), ylim=(685, 0))
    ax.axis("off")

    text(ax, 25, 26, "(a) Registration and linked identity records", 19,
         ha="left", weight="bold")
    text(ax, 25, 55, "One brand agent on one approved messaging account", 13,
         ha="left", color=MUTED)

    box(ax, 30, 88, 226, 81, "Brand / organisation", "Agent owner",
        fill=PALE_BLUE)
    arrow(ax, [(143, 170), (143, 202)])
    box(ax, 30, 204, 226, 106, "Registration", "Developer API / console\nVerify principal\nIssue credentials")
    arrow(ax, [(260, 258), (321, 258)], color=BLUE)

    ax.add_patch(Rectangle((325, 88), 565, 222, facecolor="white",
                           edgecolor=INK, linewidth=.8))
    text(ax, 607, 110, "Agent Identity Registry", 16, weight="bold")
    box(ax, 342, 137, 255, 69, "Principal", "Principal ID · verified controller",
        fill=PALE_BLUE, title_size=14, body_size=12.3)
    box(ax, 617, 137, 255, 69, "Agent identity", "Agent ID · Principal ID · public key",
        fill=PALE_BLUE, title_size=14, body_size=12.3)
    box(ax, 342, 224, 255, 69, "Channel binding", "Agent ID · account · expiry",
        title_size=14, body_size=12.3)
    box(ax, 617, 224, 255, 69, "Authorisation grant", "Principal + agent · capability scope",
        title_size=14, body_size=12.3)
    arrow(ax, [(598, 171), (615, 171)], color=MUTED)

    box(ax, 962, 88, 208, 96, "Lifecycle status", "Active · review\nSuspended · revoked",
        fill=PALE_GREEN, title_size=14)
    box(ax, 962, 214, 208, 96, "Audit history", "Issuance · updates\nChecks · decisions", title_size=14)
    arrow(ax, [(892, 137), (958, 137)], color=MUTED)
    arrow(ax, [(892, 261), (958, 261)], color=MUTED)

    ax.plot([25, 1175], [341, 341], color=RULE, lw=.8)
    text(ax, 25, 376, "(b) Verification at interaction time", 19,
         ha="left", weight="bold")
    text(ax, 25, 405, "First customer: the channel operator", 13,
         ha="left", color=MUTED)

    # Current records feed the runtime path; the channel enforces its decision.
    arrow(ax, [(744, 312), (744, 450)], color=BLUE)
    text(ax, 762, 389, "Current identity, binding,\nscope and status", 12.5,
         ha="left", color=BLUE, linespacing=1.3)

    box(ax, 30, 485, 226, 106, "Registered agent", "Short-lived signed proof\nPresented via the channel", fill=PALE_BLUE)
    arrow(ax, [(260, 538), (350, 538)])

    ax.add_patch(Rectangle((354, 453), 498, 165, facecolor=PALE_GREY,
                           edgecolor=INK, linewidth=.8))
    text(ax, 603, 476, "Verification API", 16, weight="bold")
    box(ax, 371, 501, 216, 93, "Authentication", "Signature + credential\nAgent ID + principal",
        fill="white", title_size=14)
    box(ax, 620, 501, 216, 93, "Validation", "Status + channel binding\nCapability scope",
        fill=PALE_GREEN, title_size=14)
    arrow(ax, [(590, 548), (617, 548)])
    arrow(ax, [(856, 538), (958, 538)], color=TEAL)

    box(ax, 962, 485, 208, 106, "Channel policy", "Allow / block\nVerified identity signal", fill=PALE_GREEN,
        title_size=14)
    text(ax, 25, 654, "Next phase: step-up approval and action-specific Authorisation Receipts for sensitive operations.",
         13, ha="left", color=MUTED)

    ASSETS.mkdir(parents=True, exist_ok=True)
    fig.savefig(ASSETS / "platform-overview.svg", metadata={"Date": None})
    plt.close(fig)


# Coordinates are in SVG pixels. The two layouts share all labels and symbols.
def draw_lifecycle(compact=False):
    width, height = (360, 324) if compact else (780, 282)
    svg = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg", "width": str(width),
        "height": str(height), "viewBox": f"0 0 {width} {height}",
        "role": "img", "aria-labelledby": "title desc",
        "font-family": "Arial, Helvetica, sans-serif",
    })
    ET.SubElement(svg, "title", id="title").text = "Two conversations from agent A-01"
    ET.SubElement(svg, "desc", id="desc").text = (
        "The Verification API checks the agent’s signed proof and current registry record. "
        "The channel allows the first conversation. Once the record is revoked, the channel "
        "blocks the next conversation from the same agent on account M-01."
    )

    blue, ink, muted, rule = "#295e9e", "#1c324b", "#4b6076", "#8497a9"

    def label(x, y, value, size=15, *, anchor="middle", bold=False, color=ink):
        node = ET.SubElement(svg, "text", {
            "x": str(x), "y": str(y), "text-anchor": anchor,
            "font-size": str(size), "fill": color,
            "font-weight": "600" if bold else "400",
        })
        node.text = value

    def panel(x, y, w, h, fill, radius=10):
        ET.SubElement(svg, "rect", {
            "x": str(x), "y": str(y), "width": str(w), "height": str(h),
            "rx": str(radius), "fill": fill,
        })

    def line(d, color=rule, *, end=False, dashed=False):
        attributes = {
            "d": d, "stroke": color, "fill": "none", "stroke-width": "1.6",
            "stroke-linecap": "round", "stroke-linejoin": "round",
        }
        if end:
            attributes["marker-end"] = "url(#arrow)"
        if dashed:
            attributes["stroke-dasharray"] = "3 4"
        ET.SubElement(svg, "path", attributes)

    defs = ET.SubElement(svg, "defs")
    marker = ET.SubElement(defs, "marker", {
        "id": "arrow", "viewBox": "0 0 8 8", "refX": "7", "refY": "4",
        "markerWidth": "6", "markerHeight": "6", "orient": "auto",
    })
    ET.SubElement(marker, "path", d="M1 1L7 4L1 7", fill="none", stroke=rule)

    def symbol(x, y, kind, scale=1):
        shapes = {
            "agent": "M-5 -13V-17M-6 -17H-4 M-14 -11H14Q18 -11 18 -7V10Q18 14 14 14H-14Q-18 14 -18 10V-7Q-18 -11 -14 -11Z M-8 -2V2M8 -2V2M-5 8H5",
            "gateway": "M0 -19Q9 -13 17 -12V0Q16 12 0 20Q-16 12 -17 0V-12Q-9 -13 0 -19Z M-8 0L-2 6L9 -6",
            "registry": "M-14 -8C-14 -15 14 -15 14 -8S-14 -1 -14 -8Z M-14 -8V10C-14 17 14 17 14 10V-8 M-14 1C-14 8 14 8 14 1",
        }
        ET.SubElement(svg, "path", {
            "d": shapes[kind], "transform": f"translate({x} {y}) scale({scale})",
            "fill": "#edf4fc", "stroke": blue, "stroke-width": "2.2",
            "stroke-linecap": "round", "stroke-linejoin": "round",
        })

    def decision(x, y, w, active):
        color = "#176553" if active else "#9a3943"
        panel(x, y, w, 64, "#eef7f4" if active else "#fbf1f2")
        cx, cy = x + 20, y + 39
        ET.SubElement(svg, "circle", cx=str(cx), cy=str(cy), r="9", fill="none",
                      stroke=color, attrib={"stroke-width": "1.6"})
        mark = f"M{cx-5} {cy}l3 3 6 -6" if active else f"M{cx-3} {cy-3}l6 6m0 -6l-6 6"
        line(mark, color)
        label(x+12, y+17, "First contact · Active" if active else "Next contact · Revoked",
              13, anchor="start", color=muted)
        action = "Allow" if active else "Block"
        label(x+36, y+45, action if compact else f"{action} conversation",
              17, anchor="start", bold=True, color=color)

    def registry(x, y, w):
        panel(x, y, w, 60, "#f0f5fb")
        symbol(x+25, y+29, "registry", .78)
        label(x+51, y+25, "Identity registry", 17, anchor="start", bold=True)
        label(x+51, y+46, "Verified brand · Account M-01", 14, anchor="start", color=muted)

    panel(0, 0, width, height, "#ffffff", radius=0)
    if compact:
        registry(81, 7, 269)
        line("M237 68V94", end=True, dashed=True)
        symbol(52, 117, "agent", .9)
        symbol(237, 117, "gateway", .95)
        line("M77 117H211", end=True)
        label(143, 106, "Signed proof", 13, color=muted)
        label(52, 156, "Agent A-01", 17, bold=True)
        label(52, 176, "Support agent", 13, color=muted)
        label(237, 156, "Verification API", 17, bold=True)
        label(237, 176, "Proof, binding, scope and status", 13, color=muted)
        line("M237 185V196Q237 201 232 201H182")
        label(180, 221, "Channel decision", 15, bold=True)
        line("M180 228V233H90V245", end=True)
        line("M180 233H270V245", end=True)
        decision(6, 249, 170, True)
        decision(184, 249, 170, False)
    else:
        registry(227, 12, 274)
        line("M364 73V136", end=True, dashed=True)
        symbol(86, 166, "agent", 1.18)
        symbol(364, 166, "gateway", 1.22)
        line("M116 166H334", end=True)
        label(225, 153, "Signed proof", 15, color=muted)
        label(86, 218, "Agent A-01", 20, bold=True)
        label(86, 242, "Support agent", 15, color=muted)
        label(364, 218, "Verification API", 20, bold=True)
        label(364, 242, "Proof, binding, scope and status", 15, color=muted)
        line("M395 166H480")
        line("M480 166V123Q480 117 486 117H534", end=True)
        line("M480 166V211Q480 217 486 217H534", end=True)
        label(545, 60, "Channel decision", 18, anchor="start", bold=True)
        decision(545, 85, 222, True)
        decision(545, 185, 222, False)

    ET.indent(svg)
    name = "agent-lifecycle-mobile.svg" if compact else "agent-lifecycle.svg"
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / name).write_text(ET.tostring(svg, encoding="unicode") + "\n", encoding="utf-8")


if __name__ == "__main__":
    draw_platform()
    draw_lifecycle()
    draw_lifecycle(compact=True)
