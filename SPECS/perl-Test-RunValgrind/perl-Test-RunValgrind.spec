# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-RunValgrind
Version:        0.2.2
Release:        %autorelease
Summary:        Tests that an external program is valgrind-clean
License:        MIT
URL:            https://metacpan.org/dist/Test-RunValgrind
#!RemoteAsset:  sha256:6913d14cadc251b23c5b7235f8d4ac3de287138d712b75bd94b002af0b8fa5ee
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-RunValgrind-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::Trap)

%description
valgrind is an open source and convenient memory debugger that runs on some
platforms. This module runs valgrind
(http://en.wikipedia.org/wiki/Valgrind) on an executable and makes sure
that valgrind did not find any faults in it.

%prep
%setup -q -n Test-RunValgrind-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README weaver.ini
%license LICENSE

%changelog
%autochangelog
