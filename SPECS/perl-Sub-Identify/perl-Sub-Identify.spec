# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sub-Identify
Version:        0.14
Release:        %autorelease
Summary:        Retrieve names of code references
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sub-Identify
#!RemoteAsset:  sha256:068d272086514dd1e842b6a40b1bedbafee63900e5b08890ef6700039defad6f
Source0:        https://www.cpan.org/authors/id/R/RG/RGARCIA/Sub-Identify-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-devel

%description
Sub::Identify allows you to retrieve the real name of code references.

%files -f %{name}.files
%doc Changes README.mdown TODO.mdown

%changelog
%autochangelog
