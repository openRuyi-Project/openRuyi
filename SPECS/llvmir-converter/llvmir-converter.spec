# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: YunQiang Su <yunqiang@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: Apache-2.0

%global git_ver git20260717.bdb85ba
%global git_commit bdb85ba7978db3bfeffcbd9505c43cc354e4ad6a
%global llvmir_bindir /usr/lib/llvmir-convert/bin
%global llvmir_statedir /var/lib/llvmir-converter

Name:           llvmir-converter
Version:        0+%{git_ver}
Release:        %{autorelease}
Summary:        Convert LLVM IR bitcode command files to ELF outputs
License:        Apache-2.0
URL:            https://github.com/openRuyi-Project/llvmir-converter.git
#!RemoteAsset:  sha256:e39a08bd5e8d4bff8ffbbe8673a47ab953703c7a38e4675613d5014f43bf464f
Source0:        https://github.com/openRuyi-Project/llvmir-converter/archive/%{git_commit}.tar.gz

BuildRequires:  clang22
BuildRequires:  llvm22-devel
BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  systemd-rpm-macros

Requires:       python3

%description
llvmir-converter converts LLVM IR bitcode files referenced by clang _cmd
scripts into ELF executable or shared library outputs. The package builds one
converter executable for each clang major version installed on the build host.

%prep
%autosetup -n %{name}-%{git_commit}

%build
set -eu

clang_versions=$(
    for clang in %{_bindir}/clang-[0-9]*; do
        [ -x "$clang" ] || continue
        clang_name=${clang##*/}
        clang_version=${clang_name#clang-}
        case "$clang_version" in
            ''|*[!0-9]*) continue ;;
        esac
        printf '%%s\n' "$clang_version"
    done

    if command -v clang >/dev/null 2>&1; then
        clang --version | sed -n 's/.*clang version \([0-9][0-9]*\).*/\1/p' | head -n 1
    fi
)

clang_versions=$(printf '%%s\n' $clang_versions | sort -n -u)
if [ -z "$clang_versions" ]; then
    echo "error: no installed clang versions found" >&2
    exit 1
fi

echo "Building llvmir-converter for clang versions: $clang_versions"
make clean
for clang_version in $clang_versions; do
    command -v "clang++-${clang_version}" >/dev/null 2>&1 || {
        echo "error: missing clang++-${clang_version}" >&2
        exit 1
    }
    %make_build LLVM_VER="$clang_version" CXX="clang++-${clang_version}"
done

%install
install -d -m 0755 %{buildroot}%{llvmir_bindir}
install -d -m 0755 %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_sysconfdir}/default
install -d -m 0755 %{buildroot}%{llvmir_statedir}
install -d -m 0755 %{buildroot}%{llvmir_statedir}/normal
install -d -m 0755 %{buildroot}%{llvmir_statedir}/pgo
install -d -m 1777 %{buildroot}%{llvmir_statedir}/pgo-profraw

install -m 0755 llvmir-converter-[0-9]* %{buildroot}%{llvmir_bindir}/
install -m 0755 llvmir_batch_runner.py %{buildroot}%{llvmir_bindir}/
install -m 0644 llvmir-converter.service %{buildroot}%{_unitdir}/llvmir-converter.service
install -m 0644 llvmir-converter.default %{buildroot}%{_sysconfdir}/default/llvmir-converter

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 llvmir-converter.tmpfile %{buildroot}%{_tmpfilesdir}/%{name}.conf

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%systemd_post llvmir-converter.service

%preun
%systemd_preun llvmir-converter.service

%postun
%systemd_postun_with_restart llvmir-converter.service

%files
%doc README.md CHANGELOG.md USAGE.md
%dir %{_prefix}/lib/llvmir-convert
%dir %{llvmir_bindir}
%{llvmir_bindir}/llvmir-converter-*
%{llvmir_bindir}/llvmir_batch_runner.py
%{_unitdir}/llvmir-converter.service
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/default/llvmir-converter
%dir %attr(0755,root,root) %{llvmir_statedir}
%dir %attr(0755,root,root) %{llvmir_statedir}/normal
%dir %attr(0755,root,root) %{llvmir_statedir}/pgo
%dir %attr(1777,root,root) %{llvmir_statedir}/pgo-profraw

%changelog
%autochangelog
