"use client";
import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

const TelemetryWidget = () => {
  return (
    <motion.div
      className="grid gap-4"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-xl font-semibold">Telemetry</h2>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <p className="text-sm text-gray-500">Live metrics syncing...</p>
        </CardContent>
      </Card>
    </motion.div>
  );
};

export default TelemetryWidget;
