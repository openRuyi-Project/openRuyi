# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Compress-Raw-Zlib
Version:        2.214
Release:        %autorelease
Summary:        Low-Level Interface to zlib or zlib-ng compression library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Compress-Raw-Zlib
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PM/PMQS/Compress-Raw-Zlib-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib or zlib-
ng compression libraries (see "SEE ALSO" for details about where to get
zlib or zlib-ng).

%prep
%setup -q -n Compress-Raw-Zlib-%{version}

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
