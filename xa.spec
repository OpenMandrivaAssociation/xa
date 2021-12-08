Name:		xa
Summary:	Cross-assembler for NMOS 6502 series processors
Version:	2.3.12
Release:	1
License:	GPLv2+
Group: 		Development/Tools
Url:		https://www.floodgap.com/retrotech/xa/
Source0:	https://www.floodgap.com/retrotech/xa/dists/xa-%{version}.tar.gz

%description
xa is a high-speed, two-pass portable cross-assembler. It understands mnemonics
and generates code for NMOS 6502s (such as 6502A, 6504, 6507, 6510, 7501, 8500,
8501, 8502 ...), CMOS 6502s (65C02 and Rockwell R65C02) and the 65816.
Key amongst its features:

* C-like preprocessor (and understands cpp for additional feature support)
* rich expression syntax and pseudo-op vocabulary
* multiple character sets
* binary linking
* supports o65 relocatable objects with a full linker and relocation suite,
  as well as "bare" plain binary object files
* block structure for label scoping

%prep
%autosetup -p1

%build
%make CC=%{__cc} CFLAGS="%{optflags}" LD=%{__cc} LDFLAGS="%{ldflags}"

%install
%make_install DESTDIR="%{buildroot}%{_prefix}"

%files
%{_bindir}/*
%{_mandir}/man1/*
