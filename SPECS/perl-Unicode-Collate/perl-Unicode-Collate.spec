# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Unicode-Collate
Version:        1.31
Release:        %autorelease
Summary:        Unicode Collation Algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Unicode-Collate
#!RemoteAsset:  sha256:b75dd07bbc252937b1b87064bf79ccd0a1b7ee993b8cf0e80f47406c3205639f
Source0:        https://www.cpan.org/authors/id/S/SA/SADAHIRO/Unicode-Collate-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

%description
This module is an implementation of Unicode Technical Standard #10 (a.k.a.
UTS #10) - Unicode Collation Algorithm (a.k.a. UCA).

%files -f %{name}.files
%doc Changes Collate.pmN disableXS enableXS MANIFEST.N mkheader mklocale README

%changelog
%autochangelog
