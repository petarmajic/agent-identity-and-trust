"""Draw the Agent Trust Gateway architecture and identity lifecycle scenario.

Run from the repository root: python scripts/draw_figures.py
Requires Matplotlib. The concept paper is in docs/product-concept.pdf.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle
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


def agent_mark(ax, x, y, radius=36):
    """A schematic software actor, with the same identifier at each stage."""
    corners = [(x, y-radius), (x+radius*.87, y-radius*.5),
               (x+radius*.87, y+radius*.5), (x, y+radius),
               (x-radius*.87, y+radius*.5), (x-radius*.87, y-radius*.5)]
    ax.add_patch(Polygon(corners, facecolor=PALE_BLUE, edgecolor=BLUE, lw=1))
    for dx, dy in [(-12, -9), (12, -9), (0, 13)]:
        ax.plot([x, x+dx], [y, y+dy], color=BLUE, lw=1)
        ax.add_patch(Circle((x+dx, y+dy), 3.2, facecolor="white", edgecolor=BLUE, lw=.8))
    ax.add_patch(Circle((x, y), 4.1, facecolor=BLUE, edgecolor=BLUE, lw=.8))


def outcome(ax, x, y, allowed):
    color, fill = (TEAL, PALE_GREEN) if allowed else (RED, PALE_RED)
    ax.add_patch(Circle((x, y), 29, facecolor=fill, edgecolor=color, lw=1.1))
    if allowed:
        ax.plot([x-12, x-3, x+13], [y, y+9, y-10], color=color, lw=2)
    else:
        ax.plot([x-10, x+10], [y-10, y+10], color=color, lw=2)
        ax.plot([x-10, x+10], [y+10, y-10], color=color, lw=2)
    text(ax, x, y+47, "ALLOW" if allowed else "BLOCK", 15, weight="bold", color=color)


def verification_gate(ax, y, active):
    fill, color = (PALE_GREEN, TEAL) if active else (PALE_RED, RED)
    ax.add_patch(Rectangle((350, y), 510, 104, facecolor="white", edgecolor=INK, lw=.8))
    text(ax, 373, y+24, "Verification API", 16, ha="left", weight="bold")
    ax.add_patch(Rectangle((660, y+10), 180, 28, facecolor=fill, edgecolor=color, lw=.7))
    text(ax, 750, y+24, "A-01: ACTIVE" if active else "A-01: REVOKED", 12.5, color=color, weight="bold")
    body = ("Authenticate signature and credential\nValidate principal, binding and scope"
            if active else
            "Read the current record for A-01\nRevoked identity fails verification")
    text(ax, 605, y+73, body, 14, linespacing=1.35, color=MUTED)


def draw_lifecycle():
    fig, ax = plt.subplots(figsize=(12, 8.2))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 1200), ylim=(820, 0))
    ax.axis("off")

    text(ax, 25, 28, "(a) Give the agent an identity and an approved channel", 19,
         ha="left", weight="bold")
    agent_mark(ax, 103, 177, 47)
    text(ax, 103, 247, "AI agent", 15, weight="bold")
    text(ax, 103, 274, "A-01", 16, color=BLUE)
    arrow(ax, [(165, 177), (263, 177)], color=BLUE)
    text(ax, 215, 149, "Register", 13, color=BLUE)

    # A small record excerpt makes identity continuity concrete.
    ax.add_patch(Rectangle((270, 82), 530, 220, facecolor="white", edgecolor=INK, lw=.9))
    ax.add_patch(Rectangle((270, 82), 530, 43, facecolor=PALE_BLUE, edgecolor="none"))
    text(ax, 292, 104, "Agent Identity Registry", 16, ha="left", weight="bold")
    fields = [("Agent ID", "A-01"), ("Principal", "Verified brand"),
              ("Binding", "Approved account M-01"), ("Scope", "Customer support")]
    for i, (name, value) in enumerate(fields):
        y = 150+i*40
        text(ax, 293, y, name, 14, ha="left", color=MUTED)
        text(ax, 485, y, value, 15, ha="left", weight="bold" if i == 0 else "normal",
             color=BLUE if i == 0 else INK)
        if i < 3:
            ax.plot([290, 780], [y+20, y+20], color=RULE, lw=.55)

    arrow(ax, [(804, 177), (930, 177)], color=BLUE)
    text(ax, 867, 149, "Bind", 13, color=BLUE)
    ax.add_patch(Rectangle((936, 113), 236, 128, facecolor=PALE_GREY, edgecolor=RULE, lw=.8))
    # The message outline denotes a channel, without implying a vendor integration.
    ax.add_patch(Rectangle((1035, 130), 38, 25, facecolor="white", edgecolor=MUTED, lw=.8))
    ax.plot([1040, 1040, 1048], [155, 162, 155], color=MUTED, lw=.8)
    text(ax, 1054, 183, "Business messaging", 14, weight="bold")
    text(ax, 1054, 216, "Account M-01", 14, color=MUTED)
    text(ax, 25, 333, "One stable Agent ID links the principal, approved bindings, status and audit history.",
         14, ha="left", color=MUTED)

    ax.plot([25, 1175], [358, 358], color=RULE, lw=.8)
    text(ax, 25, 389, "(b) Check the current record when the agent interacts", 19,
         ha="left", weight="bold")

    for y, active in [(473, True), (680, False)]:
        agent_mark(ax, 103, y)
        text(ax, 103, y+59, "Agent A-01", 14, weight="bold", color=BLUE)
        arrow(ax, [(149, y), (345, y)])
        text(ax, 246, y-26, "Proof · account M-01", 12.5, color=MUTED)
        verification_gate(ax, y-52, active)
        arrow(ax, [(865, y), (992, y)], color=TEAL if active else RED)
        outcome(ax, 1033, y, active)

    # Revocation is a separate authorised event, not a consequence of an allow decision.
    ax.add_patch(Rectangle((350, 558), 510, 40, facecolor=PALE_RED, edgecolor=RED, lw=.7))
    text(ax, 605, 578, "Authorised revocation · A-01: active → revoked", 14, color=RED)
    arrow(ax, [(605, 600), (605, 624)], color=RED)

    text(ax, 25, 784, "A-01 audit: registration  ·  allow decision  ·  revocation  ·  block decision",
         14, ha="left", color=MUTED)
    ASSETS.mkdir(parents=True, exist_ok=True)
    fig.savefig(ASSETS / "agent-lifecycle.svg", metadata={"Date": None})
    plt.close(fig)


if __name__ == "__main__":
    draw_platform()
    draw_lifecycle()
