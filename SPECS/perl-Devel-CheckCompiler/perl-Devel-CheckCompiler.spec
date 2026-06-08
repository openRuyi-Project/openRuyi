# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Devel-CheckCompiler
Version:        0.07
Release:        %autorelease
Summary:        Check the compiler's availability
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-CheckCompiler
#!RemoteAsset:  sha256:768b7697b4b8d4d372c7507b65e9dd26aa4223f7100183bbb4d3af46d43869b5
Source0:        https://www.cpan.org/authors/id/S/SY/SYOHEX/Devel-CheckCompiler-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::More) >= 0.98

%description
Devel::CheckCompiler is checker for compiler's availability.

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
