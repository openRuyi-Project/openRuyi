# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-ExtUtils-CChecker
Version:        0.12
Release:        %autorelease
Summary:        Configure-time utilities for using C headers, libraries, or OS features
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-CChecker
#!RemoteAsset:  sha256:8b87d145337dec1ee754d30871d0b105c180ad4c92c7dc0c7fadd76cec8c57d3
Source0:        https://www.cpan.org/authors/id/P/PE/PEVANS/ExtUtils-CChecker-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.14.0
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test2::V0)

%description
Often Perl modules are written to wrap functionality found in existing C
headers, libraries, or to use OS-specific features. It is useful in the
Build.PL or Makefile.PL file to check for the existance of these
requirements before attempting to actually build the module.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
