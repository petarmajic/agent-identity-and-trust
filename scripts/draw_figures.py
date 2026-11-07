"""Draw the Agent Trust Gateway product architecture.

Run from the repository root: python scripts/draw_figures.py
Requires Matplotlib. The concept paper is in docs/product-concept.pdf.
"""

from pathlib import Path

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


if __name__ == "__main__":
    draw_platform()
