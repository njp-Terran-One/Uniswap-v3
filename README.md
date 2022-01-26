# Uniswap-v3
uniswap simulation

**First Attempt**

The Idea

Each user ID has a Nested Dictionary (only uses relevant token pairs): {[token pair]:[tick1,tick2,liquidity,tick3,tick4,liquidity,...]}

State (for all token pairs): {[token pair]}:{[L,sqrt(P),tick]}

In this model, we'll assume that there is only 1 user in the world, and only 2 tokens in the world for the sake of simplicity. To prevent unnecessary confusions, all token pairs will be lexicographical order with token values always being of the form (x,y). So (ABC, XYZ) is a possible token pair but (XYZ,ABC) is not.

