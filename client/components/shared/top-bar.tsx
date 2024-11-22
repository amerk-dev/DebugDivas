import { cn } from "@/lib/utils";
import { Formats, Container, Filters } from "@/components/shared";

interface Props {
  className?: string;
}

export const TopBar: React.FC<Props> = ({ className }) => {
  return (
    <div
      className={cn(
        "sticky top-0 bg-white py-5 shadow-lg shadow-black/5 z-10",
        className
      )}
    >
      {" "}
      <Container className="flex items-center justify-between px-1">
        <Filters />
        <Formats />
      </Container>
    </div>
  );
};
