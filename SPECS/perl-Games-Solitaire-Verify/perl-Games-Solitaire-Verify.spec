# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Games-Solitaire-Verify
Version:        0.2601
Release:        %autorelease
Summary:        Verify solutions for solitaire games
License:        MIT
URL:            https://metacpan.org/dist/Games-Solitaire-Verify
#!RemoteAsset:  sha256:32b20e560c4b78c899a1697ef5c187f2726df9eb10e4845630687e85498ef573
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Games-Solitaire-Verify-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Dir::Manifest)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(autodie)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Getopt::Long) >= 2.36

%description
This is a CPAN Perl module that verifies the solutions of various variants
of card Solitaire. It does not aim to try to be a solver for them, because
this is too CPU intensive to be adequately done using perl5 (as of perl-
5.10.0). If you're interested in the latter, look at:

%prep
%setup -q -n Games-Solitaire-Verify-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README build-ctags.sh examples script weaver.ini
%license COPYING LICENSE

%changelog
%autochangelog
