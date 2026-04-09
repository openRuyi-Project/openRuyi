# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Temp
Version:        0.2312
Release:        %autorelease
Summary:        Return name and handle of a temporary file safely
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Temp
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/File-Temp-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl) >= 1.03
BuildRequires:  perl(File::Path) >= 2.06
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Requires:       perl(Exporter) >= 5.57
Requires:       perl(Fcntl) >= 1.03
Requires:       perl(File::Path) >= 2.06
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(parent) >= 0.221

%description
File::Temp can be used to create and open temporary files in a safe way.
There is both a function interface and an object-oriented interface. The
File::Temp constructor or the tempfile() function can be used to return the
name and the open filehandle of a temporary file. The tempdir() function
can be used to create a temporary directory.

%prep
%setup -q -n File-Temp-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README

%changelog
%autochangelog
