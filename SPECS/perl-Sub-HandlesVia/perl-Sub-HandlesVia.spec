# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sub-HandlesVia
Version:        0.053005
Release:        %autorelease
Summary:        Alternative handles_via implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sub-HandlesVia
#!RemoteAsset:  sha256:dc706e094a378a819f74eb3266ad78dabc16d941c1c5d08702d1e4cf45c9859e
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Sub-HandlesVia-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util) >= 1.54
BuildRequires:  perl(Role::Hooks) >= 0.008
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Sub::HandlesVia::XS) >= 0.002000
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny) >= 1.004
Requires:       perl(List::Util) >= 1.54
Requires:       perl(Role::Hooks) >= 0.008
Requires:       perl(Sub::HandlesVia::XS) >= 0.002000
Requires:       perl(Type::Tiny) >= 1.004

%description
If you've used Moose's native attribute traits, or MooX::HandlesVia before,
you should have a fairly good idea what this does.

%prep
%setup -q -n Sub-HandlesVia-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist
%{_fixperms} $RPM_BUILD_ROOT/*

%files -f %{name}.files
%doc CREDITS Changes README doap.ttl
%license COPYRIGHT LICENSE

%changelog
%autochangelog
