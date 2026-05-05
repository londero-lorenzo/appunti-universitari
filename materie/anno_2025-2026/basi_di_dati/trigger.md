---
title: "Trigger"
aliases: ["Trigger"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "trigger"]
created: 2026-04-14
---
```sql
CREATE or REPLACE FUNCTION <name>
RETURNS <type>
LANGUAGE plpgsql AS $$
	DECLARE
		<variable declarations>
	BEGIN
		<instructions>
	END;
$$;
```

- il corpo della funzione tra \$$ tecnicamente è una stringa

```sql
CREATE FUNCTION example_function()

```