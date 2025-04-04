import React, { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";
import { User } from "@/types/user";
import { motion } from "framer-motion";

const UsersWidget = () => {
  const [users, setUsers] = useState<User[] | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/users")
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
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
      <h2 className="text-xl font-semibold">Users</h2>
      <div className="grid gap-2">
        {loading && <Skeleton className="h-24 w-full rounded-xl" />}
        {!loading && users && users.length > 0 ? (
          users.map((user) => (
            <Card key={user.id} className="shadow-sm">
              <CardContent className="p-4">
                <p className="font-medium">{user.name}</p>
                <p className="text-sm text-gray-500">{user.email}</p>
              </CardContent>
            </Card>
          ))
        ) : (
          !loading && <p className="text-sm text-gray-400">No users found.</p>
        )}
      </div>
    </motion.div>
  );
};

export default UsersWidget;
