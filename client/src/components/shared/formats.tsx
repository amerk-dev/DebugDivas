import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from '@/components/ui'

export const Formats: React.FC = () => {
  return (
    <Select>
      <SelectTrigger className="inline-flex items-center gap-1 bg-gray-50 px-5 h-[52px] rounded-2xl cursor-pointer">
        <SelectValue placeholder="Формат:" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectLabel>Формат</SelectLabel>
          <SelectItem value="close">Ближайшие мероприятия</SelectItem>
          <SelectItem value="week">Мероприятия текущей недели</SelectItem>
          <SelectItem value="month">Мероприятия следующего месяца</SelectItem>
          <SelectItem value="quarter">Мероприятия квартала</SelectItem>
          <SelectItem value="halfyear">Мероприятия полугодия</SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
  )
}
