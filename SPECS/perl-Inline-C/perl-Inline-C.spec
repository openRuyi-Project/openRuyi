# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Inline-C
Version:        0.82
Release:        %autorelease
Summary:        C Language Support for Inline
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Inline-C
#!RemoteAsset:  sha256:10fbcf1e158d1c8d77e1dd934e379165b126a45c13645ad0be9dc07d151dd0cc
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/Inline-C-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.00
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(Inline) >= 0.86
BuildRequires:  perl(Parse::RecDescent) >= 1.967009
BuildRequires:  perl(Pegex) >= 0.66
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn) >= 0.23
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(autodie)
BuildRequires:  perl(version) >= 0.77
Requires:       perl(ExtUtils::MakeMaker) >= 7.00
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Inline) >= 0.86
Requires:       perl(Parse::RecDescent) >= 1.967009
Requires:       perl(Pegex) >= 0.66

%description
Inline::C is a module that allows you to write Perl subroutines in C. Since
version 0.30 the Inline module supports multiple programming languages and
each language has its own support module. This document describes how to
use Inline with the C programming language. It also goes a bit into Perl C
internals.

%prep
%setup -q -n Inline-C-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%files -f %{name}.files
%doc CONTRIBUTING Changes README
%license LICENSE

%changelog
%autochangelog
