import { useState } from "react";
import type { Route } from "./+types/_index";
import { useFetcher, useLoaderData, type MetaFunction } from "react-router";
import DashboardHeader from "~/components/DashboardHeader";

export function meta({}: MetaFunction) {
  return [
    { title: "Roaster" },
    { name: "description", content: "Welcome to Roaster!" },
  ];
}

export async function loader() {}

export async function action({ request }: Route.ActionArgs) {}

export default function Home() {
  return (
    <main className="p-10 font-sans">
      <DashboardHeader />
    </main>
  );
}
