# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Locale-Codes
Version:        3.86
Release:        %autorelease
Summary:        Distribution of modules to handle locale codes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Locale-Codes
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SB/SBECK/Locale-Codes-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
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

%prep
%setup -q -n Locale-Codes-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README README.first

%changelog
%autochangelog
