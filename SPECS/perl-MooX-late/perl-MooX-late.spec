# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MooX-late
Version:        0.100
Release:        %autorelease
Summary:        Easily translate Moose code to Moo
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MooX-late
#!RemoteAsset:  sha256:2ae5b1e3da5abc0e4006278ecbcfa8fa7c224ea5529a6a688acbb229c09e6a5f
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/MooX-late-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Sub::HandlesVia) >= 0.013
BuildRequires:  perl(Test::Fatal) >= 0.010
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires) >= 0.06
BuildRequires:  perl(Type::Utils) >= 1.000001
Requires:       perl(Moo) >= 2
Requires:       perl(Sub::HandlesVia) >= 0.013
Requires:       perl(Type::Utils) >= 1.000001

%description
Moo is a light-weight object oriented programming framework which aims to
be compatible with Moose. It does this by detecting when Moose has been
loaded, and automatically "inflating" its classes and roles to full Moose
classes and roles. This way, Moo classes can consume Moose roles, Moose
classes can extend Moo classes, and so forth.

%prep
%setup -q -n MooX-late-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CREDITS Changes README TODO doap.ttl
%license COPYRIGHT LICENSE

%changelog
%autochangelog
