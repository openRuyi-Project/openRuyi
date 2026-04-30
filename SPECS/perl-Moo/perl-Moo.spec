# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Moo
Version:        2.005005
Release:        %autorelease
Summary:        Minimalist Object Orientation (with Moose compatibility)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Moo
#!RemoteAsset:  sha256:fb5a2952649faed07373f220b78004a9c6aba387739133740c1770e9b1f4b108
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(threads)
Requires:       perl(Role::Tiny) >= 2.002004
Requires:       perl(Scalar::Util) >= 1.00
Requires:       perl(Sub::Defer) >= 2.006006
Requires:       perl(Sub::Quote) >= 2.006006
Requires:       perl(Exporter)
Requires:       perl(Carp)
Requires:       perl(Class::Method::Modifiers) >= 1.10

%description
This module is an extremely light-weight, high-performance Moose
replacement. It also avoids depending on any XS modules to allow simple
deployments. The name Moo is based on the idea that it provides almost -but
not quite- two thirds of Moose.

%prep
%setup -q -n Moo-%{version}

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
