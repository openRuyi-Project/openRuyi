# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Fork
Version:        0.02
Release:        %autorelease
Summary:        Test code which forks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Fork
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHWERN/Test-Fork-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder::Module) >= 0.02
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::More) >= 0.62

Requires:       perl(Test::Builder::Module) >= 0.02

%description
THIS IS ALPHA CODE! The implementation is unreliable and the interface is
subject to change.
Because each test has a number associated with it, testing code which forks
is problematic. Coordinating the test number amongst the parent and child
processes is complicated. Test::Fork provides a function to smooth over the
complications.

%prep
%setup -q -n Test-Fork-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
