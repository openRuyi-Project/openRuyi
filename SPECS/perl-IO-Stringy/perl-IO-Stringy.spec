# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Stringy
Version:        2.113
Release:        %autorelease
Summary:        IO::Stringy Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Stringy
#!RemoteAsset:  sha256:51220fcaf9f66a639b69d251d7b0757bf4202f4f9debd45bdd341a6aca62fe4e
Source0:        https://www.cpan.org/authors/id/C/CA/CAPOEIRAB/IO-Stringy-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(warnings)

Requires:       perl(Exporter) >= 5.57

%description
This toolkit primarily provides modules for performing both traditional and
object-oriented i/o) on things other than normal filehandles; in
particular, IO::Scalar, IO::ScalarArray, and IO::Lines.

%files -f %{name}.files
%doc Changes contrib examples README

%changelog
%autochangelog
