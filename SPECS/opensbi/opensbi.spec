# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           opensbi
Version:        1.8
Release:        %autorelease
Summary:        RISC-V Open Source Supervisor Binary Interface
License:        BSD-2-Clause
URL:            https://github.com/riscv-software-src/opensbi
#!RemoteAsset:  sha256:8293bca3c7507ecf15dd5dfb59fe0f700075974a1f60379f1b6626104c3f0afe
Source0:        https://github.com/riscv-software-src/opensbi/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3

%description
RISC-V Open Source Supervisor Binary Interface

%prep
%autosetup -p1 -n opensbi-%{version}

%build
make LD=ld.bfd PLATFORM=generic

%install
make LD=ld.bfd PLATFORM=generic I=%{buildroot}%{_prefix} install
install -D -m 644 COPYING.BSD %{buildroot}%{_docdir}/opensbi/COPYING.BSD
install -D -m 644 CONTRIBUTORS.md %{buildroot}%{_docdir}/opensbi/CONTRIBUTORS.md
install -D -m 644 ThirdPartyNotices.md %{buildroot}%{_docdir}/opensbi/ThirdPartyNotices.md
rm %{buildroot}%{_datadir}/opensbi/lp64/generic/firmware/fw_payload.bin
rm %{buildroot}%{_datadir}/opensbi/lp64/generic/firmware/fw_payload.elf
rm %{buildroot}%{_datadir}/opensbi/lp64/generic/firmware/payloads/test.bin
rm %{buildroot}%{_datadir}/opensbi/lp64/generic/firmware/payloads/test.elf

%files
%{_docdir}/opensbi/COPYING.BSD
%{_docdir}/opensbi/CONTRIBUTORS.md
%{_docdir}/opensbi/ThirdPartyNotices.md
%{_datadir}/opensbi/lp64/generic/firmware/fw_jump.bin
%{_datadir}/opensbi/lp64/generic/firmware/fw_dynamic.bin
%{_datadir}/opensbi/lp64/generic/firmware/fw_jump.elf
%{_datadir}/opensbi/lp64/generic/firmware/fw_dynamic.elf
%{_libdir}/lp64/opensbi/generic/lib/libplatsbi.a
%{_libdir}/lp64/libsbi.a
%{_includedir}/sbi/fw_dynamic.h
%{_includedir}/sbi/riscv_asm.h
%{_includedir}/sbi/riscv_atomic.h
%{_includedir}/sbi/riscv_barrier.h
%{_includedir}/sbi/riscv_dbtr.h
%{_includedir}/sbi/riscv_elf.h
%{_includedir}/sbi/riscv_encoding.h
%{_includedir}/sbi/riscv_fp.h
%{_includedir}/sbi/riscv_io.h
%{_includedir}/sbi/riscv_locks.h
%{_includedir}/sbi/sbi_bitmap.h
%{_includedir}/sbi/sbi_bitops.h
%{_includedir}/sbi/sbi_byteorder.h
%{_includedir}/sbi/sbi_console.h
%{_includedir}/sbi/sbi_const.h
%{_includedir}/sbi/sbi_cppc.h
%{_includedir}/sbi/sbi_csr_detect.h
%{_includedir}/sbi/sbi_dbtr.h
%{_includedir}/sbi/sbi_domain.h
%{_includedir}/sbi/sbi_domain_context.h
%{_includedir}/sbi/sbi_domain_data.h
%{_includedir}/sbi/sbi_double_trap.h
%{_includedir}/sbi/sbi_ecall.h
%{_includedir}/sbi/sbi_ecall_interface.h
%{_includedir}/sbi/sbi_emulate_csr.h
%{_includedir}/sbi/sbi_error.h
%{_includedir}/sbi/sbi_fifo.h
%{_includedir}/sbi/sbi_fwft.h
%{_includedir}/sbi/sbi_hart.h
%{_includedir}/sbi/sbi_hart_pmp.h
%{_includedir}/sbi/sbi_hart_protection.h
%{_includedir}/sbi/sbi_hartmask.h
%{_includedir}/sbi/sbi_heap.h
%{_includedir}/sbi/sbi_hfence.h
%{_includedir}/sbi/sbi_hsm.h
%{_includedir}/sbi/sbi_illegal_atomic.h
%{_includedir}/sbi/sbi_illegal_insn.h
%{_includedir}/sbi/sbi_init.h
%{_includedir}/sbi/sbi_ipi.h
%{_includedir}/sbi/sbi_irqchip.h
%{_includedir}/sbi/sbi_list.h
%{_includedir}/sbi/sbi_math.h
%{_includedir}/sbi/sbi_mpxy.h
%{_includedir}/sbi/sbi_platform.h
%{_includedir}/sbi/sbi_pmu.h
%{_includedir}/sbi/sbi_scratch.h
%{_includedir}/sbi/sbi_slist.h
%{_includedir}/sbi/sbi_sse.h
%{_includedir}/sbi/sbi_string.h
%{_includedir}/sbi/sbi_system.h
%{_includedir}/sbi/sbi_timer.h
%{_includedir}/sbi/sbi_tlb.h
%{_includedir}/sbi/sbi_trap.h
%{_includedir}/sbi/sbi_trap_ldst.h
%{_includedir}/sbi/sbi_types.h
%{_includedir}/sbi/sbi_unit_test.h
%{_includedir}/sbi/sbi_unpriv.h
%{_includedir}/sbi/sbi_version.h
%{_includedir}/sbi/sbi_visibility.h

%changelog
%{?autochangelog}
