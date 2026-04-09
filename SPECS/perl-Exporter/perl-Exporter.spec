# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Exporter
Version:        5.78
Release:        %autorelease
Summary:        Implements default import method for modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Exporter
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/T/TO/TODDR/Exporter-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.05
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod) >= 1.18
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

Requires:       perl(Carp) >= 1.05
Requires:       perl(Test::Pod) >= 1.18
Requires:       perl(Test::Pod::Coverage) >= 1.04

%description
The Exporter module implements an import method which allows a module to
export functions and variables to its users' namespaces. Many modules use
Exporter rather than implementing their own import method because Exporter
provides a highly flexible interface, with an implementation optimised for
the common case.

%prep
%setup -q -n Exporter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
