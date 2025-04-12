"use client";
import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

const NodeStatusWidget = () => {
  return (
    <motion.div
      className="grid gap-4"
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-xl font-semibold">Node Status</h2>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <p className="text-sm text-gray-500">All nodes operational ✅</p>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Document Interdependencies</h3>
          <p className="text-sm text-gray-500">Interdependencies data loading...</p>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Document Status</h3>
          <p className="text-sm text-gray-500">Status data loading...</p>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Update Related Documents</h3>
          <p className="text-sm text-gray-500">Update data loading...</p>
        </CardContent>
      </Card>
      <Card className="shadow-sm">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold">Integrate Version Control</h3>
          <p className="text-sm text-gray-500">Version control data loading...</p>
        </CardContent>
      </Card>
    </motion.div>
  );
};

export default NodeStatusWidget;
