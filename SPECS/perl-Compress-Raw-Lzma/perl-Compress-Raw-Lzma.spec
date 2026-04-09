# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Compress-Raw-Lzma
Version:        2.214
Release:        %autorelease
Summary:        Low-Level Perl Interface to lzma compression library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Compress-Raw-Lzma
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PM/PMQS/Compress-Raw-Lzma-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  pkgconfig(liblzma)

%description
Compress::Raw::Lzma provides an interface to the in-memory
compression/uncompression functions from the lzma compression library.

%prep
%setup -q -n Compress-Raw-Lzma-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
