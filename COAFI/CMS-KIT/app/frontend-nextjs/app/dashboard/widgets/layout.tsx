import React from "react";
import { Metadata } from "next";
import UsersWidget from "./widgets/UsersWidget";
import TokensWidget from "./widgets/TokensWidget"; // <-- Importa correctamente

export const metadata: Metadata = {
  title: "Dashboard | COAFI",
  description: "Federated CMS for aerospace orchestration",
};

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-gray-100 p-4 grid grid-cols-4 gap-4">
      {/* Sidebar o widgets a la izquierda */}
      <aside className="col-span-1 space-y-4">
        <UsersWidget />
        <TokensWidget /> {/* <-- Agrega como componente modular */}
        <NodeStatusWidget />
        <TelemetryWidget />
        <AIInsightsWidget />
      </aside>
      {/* Contenido principal */}
      <main className="col-span-3 bg-white rounded-xl shadow p-6">
        {children}
      </main>
    </div>
  );
}
