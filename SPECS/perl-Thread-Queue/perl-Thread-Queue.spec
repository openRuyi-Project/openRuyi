# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Thread-Queue
Version:        3.13
Release:        %autorelease
Summary:        Thread-safe queues
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Thread-Queue
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/J/JD/JDHEDDEN/Thread-Queue-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.1
BuildRequires:  perl(Test::More) >= 0.5
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(threads::shared) >= 1.21

Requires:       perl(Scalar::Util) >= 1.1
Requires:       perl(Test::More) >= 0.5
Requires:       perl(threads::shared) >= 1.21

%description
This module provides thread-safe FIFO queues that can be accessed safely by
any number of threads.

%prep
%setup -q -n Thread-Queue-%{version}

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
