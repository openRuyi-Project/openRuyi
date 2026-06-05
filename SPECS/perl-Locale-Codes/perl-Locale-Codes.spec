# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Locale-Codes
Version:        3.90
Release:        %autorelease
Summary:        Distribution of modules to handle locale codes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Locale-Codes
#!RemoteAsset:  sha256:984cd90bdc99e85316fc9553353e44363cd317dcde9e4d24f4dac45bc6feb46d
Source0:        https://www.cpan.org/authors/id/S/SB/SBECK/Locale-Codes-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(if)
BuildRequires:  perl(Test::Inter) >= 1.09
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

%description
Locale-Codes is a distribution containing a set of modules designed to work
with sets of codes which uniquely identify something. For example, there
are codes associated with different countries, different currencies,
different languages, etc. These sets of codes are typically maintained in
some standard.

%files -f %{name}.files
%doc Changes README README.first

%changelog
%autochangelog
