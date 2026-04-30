# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-TreeCreate
Version:        0.0.1
Release:        %autorelease
Summary:        Recursively create a directory tree
License:        MIT
URL:            https://metacpan.org/dist/File-TreeCreate
#!RemoteAsset:  sha256:57686f10843be81affad185ae4131790ba0c4af36d2104d6fb69126528055267
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-TreeCreate-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(autodie)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
This module was extracted from several near-identical copies used in the
tests of some of my CPAN distributions.

%prep
%setup -q -n File-TreeCreate-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --installdirs=vendor --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README weaver.ini
%license LICENSE

%changelog
%autochangelog
