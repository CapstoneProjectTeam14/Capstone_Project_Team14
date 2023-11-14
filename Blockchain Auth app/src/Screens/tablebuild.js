import { useTable } from "react-table";
import React from "react";
const MyTable = ({ data }) => {
  const columns = React.useMemo(
    () => [
      {
        Header: "Device ID",
        accessor: "deviceId", // accessor is the "key" in the data
      },
      {
        Header: "State",
        accessor: "state",
      },
      {
        Header: "Packets",
        accessor: "packets",
      },

     {
      Header: 'ETH Type',
      accessor: 'selector.criteria[0].ethType', 
    }, 

      {
        Header: "Last Seen",
        accessor: "lastSeen",
        Cell: ({ value }) => new Date(value).toLocaleString(),
      },
    ],
    []
  );

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    useTable({ columns, data });

  return (
    <table
      {...getTableProps()}
      style={{ borderCollapse: "collapse", width: "100%" }}
    >
      <thead>
        {headerGroups.map((headerGroup) => (
          <tr {...headerGroup.getHeaderGroupProps()}>
            {headerGroup.headers.map((column) => (
              <th
                {...column.getHeaderProps()}
                style={{ border: "1px solid black", padding: "8px" }}
              >
                {column.render("Header")}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map((row) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()} key={row.id}>
              {row.cells.map((cell) => (
                <td
                  {...cell.getCellProps()}
                  style={{ border: "1px solid black", padding: "8px" }}
                >
                  {cell.render("Cell")}
                </td>
              ))}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};
export default MyTable;
