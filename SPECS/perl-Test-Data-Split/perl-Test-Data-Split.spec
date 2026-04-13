# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Data-Split
Version:        0.2.2
Release:        %autorelease
Summary:        Split data-driven tests into several test scripts
License:        MIT
URL:            https://metacpan.org/dist/Test-Data-Split
#!RemoteAsset:  sha256:e5083890adad30d7de50703569d5f5cef174a198593522ea7b46ce387b828022
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-Data-Split-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(MooX)
BuildRequires:  perl(MooX::late) >= 0.010
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(autodie)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(MooX::late) >= 0.010

%description
This module splits a set of data with IDs and arbitrary values into one
test file per (key+value) for easy parallelisation.

%prep
%setup -q -n Test-Data-Split-%{version}

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
