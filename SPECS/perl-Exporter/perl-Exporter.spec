# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Exporter
Version:        5.79
Release:        %autorelease
Summary:        Implements default import method for modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Exporter
#!RemoteAsset:  sha256:229459746e6933aabad983aafee125a9fad492db49af2887509eb4311287d7a2
Source0:        https://www.cpan.org/authors/id/T/TO/TODDR/Exporter-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
