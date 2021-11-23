cubosem = {
	'+' : {
		'int' : {
			'int' 	: 'int',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'char' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'bool' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'float' : {
			'int' : 'float',
			'float' : 'float',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'string',
			'string' : 'string'
		}
	},

	'-' : {
		'int' : {
			'int' 	: 'int',
			'char' 	: 'error',
			'bool' 	: 'error',
			'float' : 'float',
			'string': 'error'
		},
		'char' : {
			'int' 	: 'error',
			'char' 	: 'error',
			'bool' 	: 'error',
			'float' : 'error',
			'string': 'error'
		},
		'bool' : {
			'int' 	: 'error',
			'char' 	: 'error',
			'bool' 	: 'error',
			'float' : 'error',
			'string': 'error'
		},
		'float' : {
			'int' : 'float',
			'float' : 'float',
			'char' : 'error',
			'bool' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'char' : 'error',
			'bool' : 'error',
			'float' : 'error',
			'string' : 'error'
		}
	},

	'*' : {
		'int' : {
			'int' 	: 'int',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'char' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'bool' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'float' : {
			'int' 	: 'float',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'string' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		}
	},

	'/' : {
		'int' : {
			'int' 	: 'int',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'char' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'bool' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'float' : {
			'int' 	: 'float',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		},
		'string' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
			'string': 'error'
		}
	},

	'=' : {
		'int' : {
			'int' : 'int',
			'float' : 'int',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'float',
			'float' : 'float',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'bool',
			'char' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'char',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'string'
		}
	},

	'==' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error',
				'string' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error',
				'string' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool',
				'string' : 'error'
			},
			'string' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'string'
			}
		},

	'!=' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error',
				'string' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error',
				'string' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool',
				'string' : 'error'
			},
			'string' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'string'
			}
		},

	'<' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error',
				'string' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error',
				'string' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool',
				'string' : 'error'
			},
			'string' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'string'
			}
		},

	'>' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error',
				'string' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error',
				'string' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool',
				'string' : 'error'
			},
			'string' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'string'
			}
		},

	'<=' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error',
				'string' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error',
				'string' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool',
				'string' : 'error'
			},
			'string' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'string'
			}
		},

	'>=' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error',
				'string' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error',
				'string' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool',
				'string' : 'error'
			},
			'string' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'string'
			}
		},

	'&' : {
		'int' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'bool',
			'char' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		}
	},

	'|' : {
		'int' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'char' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'bool' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'bool',
			'char' : 'error',
			'string' : 'error'
		},
		'float' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},
		'string' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		}
	},

}

cubosemCont = {
	'++' : {
			'int' : 'int',
			'float' : 'float',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		},

	'--' : {
			'int' : 'int',
			'float' : 'float',
			'bool' : 'error',
			'char' : 'error',
			'string' : 'error'
		}
	}

def CuboSemRes(operacion, izq, der):
	return cubosem[operacion][izq][der]

def CuboSemContRes(operador, var1):
	return cubosemCont[operador][var1]
