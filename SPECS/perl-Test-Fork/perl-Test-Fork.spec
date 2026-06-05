# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Fork
Version:        0.02
Release:        %autorelease
Summary:        Test code which forks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Fork
#!RemoteAsset:  sha256:fcfefbfb24f885abe827c2ad07ac3d4e1fecf213a14717fcaf3c37175045d03e
Source0:        https://www.cpan.org/authors/id/M/MS/MSCHWERN/Test-Fork-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Module) >= 0.02
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::More) >= 0.62

Requires:       perl(Test::Builder::Module) >= 0.02

%description
THIS IS ALPHA CODE! The implementation is unreliable and the interface is
subject to change.

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
