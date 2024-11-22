"use client";

import { Search } from "lucide-react";
import { useRef, useState } from "react";
import { useClickAway, useDebounce } from "react-use";
// import { Api } from "@/shared/service/api-client";
import { cn } from "@/lib/utils";

interface Props {
  classname?: string;
}

export const SearchInput: React.FC<Props> = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [events, setEvents] = useState<string[]>([]);
  console.log("events: ", events);
  const [focused, setFocused] = useState(false);
  const ref = useRef(null);
  useClickAway(ref, () => {
    setFocused(false);
  });

  const response = ["a", "b", "c"];

  useDebounce(
    async () => {
      try {
        // const response = await Api.products.search(searchQuery);
        setEvents(response);
      } catch (error) {
        console.error(error);
      }
    },
    250,
    [searchQuery]
  );

  return (
    <>
      {focused && (
        <div className="fixed top-0 left-0 bottom-0 right-0 bg-black/50 z-30" />
      )}
      <div
        ref={ref}
        className={cn(
          "flex rounded-2xl flex-1 justify-between relative h-11",
          focused && "z-30"
        )}
      >
        <Search className="absolute top-1/2 translate-y-[-50%] left-3 h-5 text-gray-400" />

        <input
          className="rounded-2xl outline-none w-full bg-gray-50 pl-11"
          type="text"
          placeholder="Найти мероприятие..."
          onFocus={() => setFocused(true)}
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </div>
    </>
  );
};
