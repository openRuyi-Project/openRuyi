# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Term-Cap
Version:        1.18
Release:        %autorelease
Summary:        Perl termcap interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Term-Cap
#!RemoteAsset:  sha256:7d5b155824223b4c5cc2587b9dea15f7a5c8f7fd9eaf704a9a6828557a527d0a
Source0:        https://www.cpan.org/authors/id/J/JS/JSTOWE/Term-Cap-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.33

Requires:       perl(Test::More) >= 0.33

%description
These are low-level functions to extract and use capabilities from a
terminal capability (termcap) database.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
