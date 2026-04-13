# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-All
Version:        0.87
Release:        %autorelease
Summary:        IO::All Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-All
#!RemoteAsset:  sha256:54e21d250c0229127e30b77a3461e10077854ec244f26fb670f1b445ed4c4d5b
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/IO-All-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)

Requires:       perl(File::Copy)
Requires:       perl(File::Path)
Requires:       perl(IO::Handle)
Requires:       perl(Tie::File)
Requires:       perl(warnings)

%description
The IO::All object is a proxy for IO::File, IO::Dir, IO::Socket,
IO::String, Tie::File, File::Spec, File::Path and File::ReadBackwards; as
well as all the DBM and MLDBM modules. You can use most of the methods
found in these classes and in IO::Handle (which they inherit from). IO::All
adds dozens of other helpful idiomatic methods including file stat and
manipulation functions.

%prep
%setup -q -n IO-All-%{version}

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
