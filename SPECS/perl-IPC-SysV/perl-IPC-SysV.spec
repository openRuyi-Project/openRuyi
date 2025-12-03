# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IPC-SysV
Version:        2.09
Release:        %autorelease
Summary:        System V IPC constants and system calls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IPC-SysV
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MH/MHX/IPC-SysV-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.45

Requires:       perl(Test::More) >= 0.45

%description
IPC::SysV defines and conditionally exports all the constants defined in
your system include files which are needed by the SysV IPC calls. Common
ones include

%prep
%setup -q -n IPC-SysV-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes const-c.inc const-xs.inc README TODO

%changelog
%{?autochangelog}
