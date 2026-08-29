# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Compress-Raw-Zlib
Version:        2.222
Release:        %autorelease
Summary:        Low-Level Interface to zlib or zlib-ng compression library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Compress-Raw-Zlib
#!RemoteAsset:  sha256:1dfd7d511a655627c81815d30d3babc28fa5b88455ff03f8b04099dcb51286b8
Source0:        https://www.cpan.org/authors/id/P/PM/PMQS/Compress-Raw-Zlib-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib or zlib-
ng compression libraries (see "SEE ALSO" for details about where to get
zlib or zlib-ng).

%files -f %{name}.files
%doc Changes README SECURITY.md

%changelog
%autochangelog
