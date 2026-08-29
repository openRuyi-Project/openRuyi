# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Mouse
Version:        2.6.2
Release:        %autorelease
Summary:        Moose minus the antlers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Mouse
#!RemoteAsset:  sha256:3ab8b0f9f96cbe43ff23498d900f91add52455dc9a7d6613a0a8186142bdeecf
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYOHEX/Mouse-v%{version}.tar.gz
BuildSystem:    perlbuild

BuildOption(prep):  -n Mouse-v%{version}
BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(Devel::PPPort) >= 3.59
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.22
BuildRequires:  perl(Module::Build) >= 0.4005
BuildRequires:  perl(Module::Build::XSUtil) >= 0.19
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)

%description
Mouse is a lightweight object system for Perl with a Moose-like interface.

%files -f %{name}.files
%doc Changes README.md example
%license LICENSE

%changelog
%autochangelog
