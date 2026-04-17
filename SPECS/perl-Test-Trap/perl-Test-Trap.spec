# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Trap
Version:        0.3.5
Release:        %autorelease
Summary:        Trap exit codes, exceptions, output, etc
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Trap
#!RemoteAsset:  sha256:54f99016562b5b1d72110100f1f2be437178cdf84376f495ffd0376f1d7ecb9a
Source0:        https://cpan.metacpan.org/authors/id/E/EB/EBHANSSEN/Test-Trap-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester) >= 0.107
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
Requires:       perl(Test::Tester) >= 0.107

%description
Primarily (but not exclusively) for use in test scripts: A block eval on
steroids, configurable and extensible, but by default trapping (Perl)
STDOUT, STDERR, warnings, exceptions, would-be exit codes, and return
values from boxed blocks of test code.

%prep
%setup -q -n Test-Trap-v%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README xt
%license

%changelog
%autochangelog
