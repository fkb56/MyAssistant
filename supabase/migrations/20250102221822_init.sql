CREATE OR REPLACE FUNCTION public.create_user()
    RETURNS trigger
    LANGUAGE plpgsql
    SECURITY DEFINER
AS
$function$
BEGIN
    INSERT INTO public.users (id)
    VALUES (NEW.id);
    RETURN NEW;
END;
$function$;

-- Trigger
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW
    EXECUTE FUNCTION public.create_user();