# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Type-Tiny
Version:        2.010001
Release:        %autorelease
Summary:        Tiny, yet Moo(se)-compatible type constraint
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Type-Tiny
#!RemoteAsset:  sha256:cd583e4983039f35052d490f0c4439124ba667d4f09c4e3aec47de5200f9921a
Source0:        http://www.cpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Exporter::Tiny) >= 1.006000
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Text::Balanced)

Requires:       perl(Exporter::Tiny) >= 1.006000

%description
Type::Tiny is a small class for creating Moose-like type constraint objects
which are compatible with Moo, Moose and Mouse.

%prep
%setup -q -n Type-Tiny-%{version}

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
