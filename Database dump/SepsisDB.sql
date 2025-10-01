--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2025-10-01 11:17:06

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 216682)
-- Name: patients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patients (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    address character varying(200),
    phone character varying(20),
    age integer,
    gender character varying(10),
    hr double precision,
    o2sat double precision,
    temp double precision,
    map double precision,
    resp double precision,
    bun double precision,
    chloride double precision,
    creatinine double precision,
    glucose double precision,
    hct double precision,
    hgb double precision,
    wbc double precision,
    platelets double precision,
    hosp_adm_time double precision,
    iculos double precision,
    prediction character varying(50),
    probability double precision
);


ALTER TABLE public.patients OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 216681)
-- Name: patients_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.patients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.patients_id_seq OWNER TO postgres;

--
-- TOC entry 4851 (class 0 OID 0)
-- Dependencies: 217
-- Name: patients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.patients_id_seq OWNED BY public.patients.id;


--
-- TOC entry 4695 (class 2604 OID 216685)
-- Name: patients id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients ALTER COLUMN id SET DEFAULT nextval('public.patients_id_seq'::regclass);


--
-- TOC entry 4844 (class 0 OID 216682)
-- Dependencies: 218
-- Data for Name: patients; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patients (id, name, address, phone, age, gender, hr, o2sat, temp, map, resp, bun, chloride, creatinine, glucose, hct, hgb, wbc, platelets, hosp_adm_time, iculos, prediction, probability) FROM stdin;
1	omar	Jayd	010101010	2313	Male	25	21	38	44	44	42	123	23132	231313	2132132	132	123	1	21	321	No HAI	0.44
12	johny	adasasd	121561	53	Female	84	100	36	103	18	34	105	3.9	65	32.3	11.4	7.5	127	-85.9	8	HAI	0.72
13	johny	adasasd	121561	53	Male	84	100	36	103	18	34	105	3.9	65	32.3	11.4	7.5	127	-85.9	8	HAI	0.82
9	asda	nasr city	0121212	53	Female	84	100	36	103	18	34	105	4	65	32	11	7.5	127	85	8	No HAI	0.38666666666666666
14	ali	nein	1231313	88	Male	84	80	38	55	55	55	12	23	15	112	1212	11	28	-5	1	No HAI	0.4266666666666667
10	hossam	nasr city	0121212	53	Male	84	100	36	103	18	34	105	4	65	32	11	7.5	127	-85	8	No HAI	0.37666666666666665
16	5651	623	61	32	Female	132	132	13	13	213	132	132	132	13	213	132	1321	321	132	132	No HAI	0.44666666666666666
17	5651	623	61	32	Female	132	132	13	13	213	132	132	132	13	213	132	1321	321	132	132	No HAI	0.44666666666666666
18	151	3213	21	1321	Female	13	1	321	231	312	313	21	3213	21	2313	21	3213	13	3	12	No HAI	0.35333333333333333
19	151	3213	21	1321	Female	13	1	321	231	312	313	21	3213	21	2313	21	3213	13	3	12	No HAI	0.35333333333333333
20	11	2123	313	23	Female	13	132	45	1	3213	213	2132	13	213	21	321	32	1321	123	132	No HAI	0.49
21	Omar Testing Positive	New Cairo	011111111	88	Male	97	93	38	71	23	15	108	0.7	168	30.5	10.2	17.5	257	-0.3	37	HAI	0.5666666666666667
24	Positive HAI Test	Cairo	01000000	88	Male	97	93	38	71	23	15	108	0.7	168	30	10	18	257	-0.3	37	HAI	0.5633333333333334
26	Omar Negative	Giza	020000	30	Male	100	100	37	80	23	15	108	0.5	150	30	10	17	300	5	0	No HAI	0.12333333333333334
\.


--
-- TOC entry 4852 (class 0 OID 0)
-- Dependencies: 217
-- Name: patients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.patients_id_seq', 26, true);


--
-- TOC entry 4697 (class 2606 OID 216687)
-- Name: patients patients_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (id);


--
-- TOC entry 4850 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2025-10-01 11:17:07

--
-- PostgreSQL database dump complete
--

