import Link from "next/link";
import { cn } from "@/lib/utils";
import { Container, SearchInput } from "@/src/components/shared";

interface Props {
  className?: string;
}

export const Header: React.FC<Props> = ({ className }) => {
  return (
    <header className={cn(" border-b", className)}>
      <Container className="flex items-center justify-between py-8">
        <Link href="/">
          <div className="flex items-center gap-4">
            {/* <Image src="/logo.png" alt="logo" width={35} height={35} /> */}
            <div className="">
              <h1 className="text-2xl uppercase font-black">Мероприятия</h1>
            </div>
          </div>
        </Link>

        <div className="mx-10 flex-1">
          <SearchInput />
        </div>
      </Container>
    </header>
  );
};
