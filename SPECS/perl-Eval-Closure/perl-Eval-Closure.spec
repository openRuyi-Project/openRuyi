# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Eval-Closure
Version:        0.14
Release:        %autorelease
Summary:        Safely and cleanly create closures via string eval
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Eval-Closure
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DO/DOY/Eval-Closure-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(B)
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::LexAlias) >= 0.05
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(overload)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(warnings)

Requires:       perl(Devel::LexAlias) >= 0.05

%description
String eval is often used for dynamic code generation. For instance, Moose
uses it heavily, to generate inlined versions of accessors and
constructors, which speeds code up at runtime by a significant amount.
String eval is not without its issues however - it's difficult to control
the scope it's used in (which determines which variables are in scope
inside the eval), and it's easy to miss compilation errors, since eval
catches them and sticks them in $@ instead.

%prep
%setup -q -n Eval-Closure-%{version}

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
