package br.inatel.labs.labrest.server.model;

import java.math.BigDecimal;

public class Produto {
	
	private Long id;
	private String descricao;
	private BigDecimal preco;
	
	public Produto(Long id, String descricao, BigDecimal preco) {
		this.setDescricao(descricao);
		this.setId(id);
		this.setPreco(preco);		
	}
	
	public Produto() {
		
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public BigDecimal getPreco() {
		return preco;
	}

	public void setPreco(BigDecimal preco) {
		this.preco = preco;
	}

}
