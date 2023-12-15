-- creates an index on the table names and first letter of name
CREATE INDEX idx_name_first ON names(name(1));
