"use client";

import React, { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";
import { motion } from "framer-motion";

// Modelo del token
type Token = {
  id: string;
  name: string;
  symbol: string;
  balance: number;
};

const TokensWidget = () => {
  const [tokens, setTokens] = useState<Token[] | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/tokens") // Cambia a tu endpoint real
      .then((res) => res.json())
      .then((data) => {
        setTokens(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <motion.div
      className="grid gap-4"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-xl font-semibold">Tokens</h2>
      <div className="grid gap-2">
        {loading && <Skeleton className="h-24 w-full rounded-xl" />}
        {!loading && tokens && tokens.length > 0 ? (
          tokens.map((token) => (
            <Card key={token.id} className="shadow-sm">
              <CardContent className="p-4">
                <div className="flex justify-between items-center">
                  <p className="font-medium">{token.name} ({token.symbol})</p>
                  <p className="text-sm text-gray-500">{token.balance}</p>
                </div>
              </CardContent>
            </Card>
          ))
        ) : (
          !loading && <p className="text-sm text-gray-400">No tokens found.</p>
        )}
      </div>
    </motion.div>
  );
};

export default TokensWidget;
