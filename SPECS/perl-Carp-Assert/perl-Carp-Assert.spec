# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Carp-Assert
Version:        0.22
Release:        %autorelease
Summary:        Executable comments
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Carp-Assert
#!RemoteAsset:  sha256:807ea97c6bed76ac2e4969efba7dae48fefeb9f28797f112671b3ac8a49355f7
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Carp-Assert-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

Requires:       perl(Role::Tiny) >= 2.002004
Requires:       perl(Scalar::Util) >= 1.00
Requires:       perl(Sub::Defer) >= 2.006006
Requires:       perl(Sub::Quote) >= 2.006006
Requires:       perl(Exporter)
Requires:       perl(Carp)
Requires:       perl(Class::Method::Modifiers) >= 1.10

%description
Carp::Assert is intended for a purpose like the ANSI C library assert.h.

%prep
%setup -q -n Carp-Assert-%{version}

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
